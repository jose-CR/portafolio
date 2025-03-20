<section class="flex items-center justify-center">
    <table class="min-w-full table-auto border border-gray-300 dark:border-gray-600">
        <thead class="bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-gray-100 text-center">
            <tr class="">
                <th class="px-4 py-2 border-r border-gray-300 dark:border-gray-600">Name</th>
                <th class="px-4 py-2 border-r border-gray-300 dark:border-gray-600">Image</th>
                <th class="px-4 py-2 border-r border-gray-300 dark:border-gray-600">Description</th>
                <th class="px-4 py-2">Settings</th>
            </tr>
        </thead>
    
        <!-- Cuerpo de la tabla -->
        <tbody class="bg-white dark:bg-gray-800 text-center text-pretty">
            @foreach ($projects as $project)
                <tr class="border-b border-gray-300 dark:border-gray-600 text-black dark:text-white">
                    <td class="px-4 py-2 border-r border-gray-300 dark:border-gray-600">{{ $project->project_name }}</td>
                    <td class="px-4 py-2 border-r border-gray-300 dark:border-gray-600 flex justify-center items-center">
                        <img src="{{ asset('storage/' . $project->image_url) }}" alt="image" class="w-16 h-16 object-cover rounded">
                    </td>
                    <td class="px-4 py-2 border-r border-gray-300 dark:border-gray-600">{{ $project->project_description }}</td>
                    <td class="px-4 py-2">
                        <livewire:profile.ui.dropdown :project="$project" />
                    </td>
                </tr>
            @endforeach
        </tbody>
    </table>    
</section>
