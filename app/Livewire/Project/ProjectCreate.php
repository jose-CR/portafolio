<?php

namespace App\Livewire\Project;

use Livewire\Component;
use Livewire\WithFileUploads;
use App\Models\Project;
use Illuminate\Support\Facades\Storage;

class ProjectCreate extends Component
{

    use WithFileUploads;

    public $project_name;
    public $project_description;
    public $image_url;

    protected $rules = [
        'project_name' => 'required|string|max:255',
        'project_description' => 'required|string',
        'image_url' => 'nullable|image|max:2048', // 2MB máximo
    ];

    public function saveProject()
    {
        $this->validate();

        $imagePath = null;
        if ($this->image_url) {
            $imagePath = $this->image_url->store('img/projects', 'public'); // Guarda la imagen en storage/app/public/projects
        }

        Project::create([
            'project_name' => $this->project_name,
            'project_description' => $this->project_description,
            'image_url' => $imagePath,
        ]);

        // Limpiar formulario después de guardar
        $this->reset(['project_name', 'project_description', 'image_url']);

        // Emitir evento de éxito
        session()->flash('message', 'Project created successfully!');
    }

    public function render()
    {
        return view('livewire.project.project-create');
    }
}
